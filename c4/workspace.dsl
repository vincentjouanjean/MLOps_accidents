workspace "Name" "Description" {

    !identifiers hierarchical

    model {
        policier = person "Policier"
        admin = person "Admin"
        loginss = softwareSystem "Login system" {
            loginAPI = container "Login API" {
                main = component "Runner" {
                    tags "Python"
                }
                api = component "API" "FastAPI" {
                    tags "Python", "FastAPI"
                }
                domain = component "Domain" "Python" {
                    tags "Python", "domain"
                }
                repository_jdbc = component "JDBC repository" "sqlalchemy" {
                    tags "Python", "sqlalchemy"
                }
                repository_jwt = component "JWT repository" "authlib" {
                    tags "Python"
                }
                main -> api "uses" "Python"
                api -> domain "calls" "Python"
                repository_jdbc -> domain "implements" "sqlalchemy"
                repository_jwt -> domain "implements" "authlib"
            }
            login_db = container "Login Database" "User storage" "PostgreSQL" {
                tags "Database"
            }
            loginAPI.repository_jdbc -> login_db "read/write" "sql"
        }
        train_software_system = softwareSystem "Apprentissage du modèle de prédiction de la gravité des accidents de la route" {
            group steps {
                init = container "0. Training launcher" "Expose endpoint to run a new experiment" "Python" {
                    tags "Python", "FastAPI"
                }
                extract = container "1. Extract data" "Extract data from external system and save it in repository" "Python" {
                    tags "Python"
                }
                transform = container "2. Transform data" "Transform data and save it in repository" "Python" {
                    tags "Python"
                }
                training = container "3. & 4. Model training / Model Repository" "Model training, save experiments, and manage deploiement workflow" "Python" {
                    tags "Python"
                    training_model = component "3. Training model" "Training model and push experiment to repository" "Python" {
                        tags "Python"
                    }
                    training_api = component "4. Deploiement workflow API" "API to manage deploiements and deploy model" "FastAPI" {
                        tags "Python", "FastAPI"
                    }
                    mlflow = component "Model Storage" "Store, vizualize mobel performance and manage deploiement deploiement" "MLFlow" {
                        tags "ExternalTool"
                    }
                    training_model -> mlflow "push" "experiment"
                    training_api -> mlflow "model selection" "http"
                    training_api -> mlflow "load" "sdk"
                    training_model -> training_api {
                        tags "step"
                    }
                }
                init -> extract {
                    tags "step"
                }
                extract -> transform {
                    tags "step"
                }
                transform -> training {
                    tags "step"
                }
            }
            lakefs = container "Data repository" "Store training data" "LakeFS" {
                tags "ExternalTool"
            }

            streaming = container "Streaming" "Use it to sequence the model training workflow" "Kafka" {
                tags "Streaming"
            }

            redis = container "Expose model" "Store the lastest version of the model" "Redis" {
                tags "Database"
            }

            init -> streaming "produce" "streaming"
            extract -> streaming "consume/produce" "streaming"
            extract -> streaming "produce" "streaming"
            transform -> streaming "consume" "streaming"
            transform -> streaming "produce" "streaming"
            training.training_model -> streaming "consume" "streaming"

            extract -> lakefs "push data" "http"
            transform -> lakefs "read&push data/pull request" "http"
            training -> lakefs "read data" "http"
            training.training_api -> lakefs "merge" "http"
            training.training_model -> lakefs "read" "experiment"
            training.training_api -> redis "cache model" "http"
        }
        service_sofware_system = softwareSystem "Service de prédiction de la gravité des accidents de la route" {
            front = container "Web Application" "IHM" "Vue" {
                tags "TODO"
            }
            bff = container "Back for frontend" "Separate backend services to frontend application" "Python" {
                tags "TODO"
            }
            predictAPI = container "Prediction API" "Use model to predict and store history in dedicated database" {
                tags "Python"
                main = component "Runner" {
                    tags "Python"
                }
                api = component "API" "FastAPI" {
                    tags "Python", "FastAPI"
                }
                domain = component "Domain" "Python" {
                    tags "Python", "domain"
                }
                repository_jdbc = component "JDBC repository" "sqlalchemy" {
                    tags "Python", "sqlalchemy"
                }
                repository_predict = component "Prediction repository" "sklearn/redis" {
                    tags "Python"
                }
                main -> api "uses" "Python"
                api -> domain "calls" "Python"
                repository_jdbc -> domain "implements" "sqlalchemy"
                repository_predict -> domain "implements" "sklearn/redis"
            }
            predict_db = container "Prediction Database" "Store history" "MongoDB" {
                tags "Database"
            }
            front -> bff "Uses"

            bff -> loginss.loginAPI "read/write" "http"
            bff -> predictAPI "read/write" "http"

            predictAPI -> loginss.loginAPI "read" "http"
            predictAPI.repository_jdbc -> predict_db "read/write" "sql"
            predictAPI.repository_predict -> train_software_system.redis "load model" "http"
        }

        policier -> service_sofware_system.front "Get prediction" "web"
        admin -> service_sofware_system.front "Show history" "web"
        admin -> train_software_system.training.training_api "Chose model" "web"
        admin -> train_software_system.init "write" "http"
        admin -> train_software_system.lakefs "read/compare data" "web"
        admin -> train_software_system.training.mlflow "Visualize models and metrics" "web"
    }

    views {
        systemContext service_sofware_system "Level_1" {
            include *
            autolayout lr
        }

        container service_sofware_system "service_sofware_system_Level_2" {
            include *
            autolayout lr
        }

        container train_software_system "train_software_system_Level_2_without_streaming" {
            include *
            exclude train_software_system.streaming
            autolayout tb

            animation {
                admin
                train_software_system.init
                train_software_system.extract
                train_software_system.lakefs
                train_software_system.transform
                train_software_system.training
                train_software_system.redis
            }
        }

        component service_sofware_system.predictAPI "service_sofware_system_Level_3" {
            include *
            autolayout lr
        }

        container train_software_system "train_software_system_Level_2" {
            include *
            autolayout tb

            animation {
                admin
                train_software_system.init
                train_software_system.streaming
                train_software_system.extract
                train_software_system.lakefs
                train_software_system.transform
                train_software_system.training
                train_software_system.redis
            }
        }

        component loginss.loginAPI "login_Level_3" {
            include *
            autolayout lr
        }

        component train_software_system.training "training_Level_3" {
            include *
            autolayout tb

            animation {
                train_software_system.streaming
                train_software_system.lakefs
                train_software_system.training.training_model
                train_software_system.training.mlflow
                admin
                train_software_system.training.training_api
                train_software_system.redis
            }
        }

        styles {
            relationship "step" {
                color #2200ff
                style solid
                thickness 0
            }
            element "Element" {
                color #ffffff
            }
            element "Person" {
                background #0000ff
                shape person
            }
            element "Software System" {
                background #f86628
            }
            element "Container" {
                background #f88728
            }
            element "Database" {
                shape cylinder
                background #10136b
            }
            element "ExternalTool" {
                shape diamond
                background #ff0000
            }
            element "Streaming" {
                shape pipe
                background #555555
            }
            element "domain" {
                shape hexagon
                background #ff008f
            }
            element "Python" {
                shape pipe
                background #ff008f
            }
            element "TODO" {
                shape pipe
                background #555555
            }
        }
    }

    configuration {
        #scope softwaresystem
    }

}
