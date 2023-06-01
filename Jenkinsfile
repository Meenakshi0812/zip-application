pipeline {
    agent any
    
    environment {
        folderName = sh(script: 'date +"%Y%m%d%H%M%S"', returnStdout: true).trim()
    }
    
    stages {
        stage('Clean Workspace') {
            steps {
                sh 'rm -rf zip-application'
            }
        }
        
        stage('Clone Repository as Zip') {
            steps {
                script {
                    sh 'git clone --depth 1 https://github.com/Meenakshi0812/zip-application.git zip-application'
                    sh "zip -r ${env.folderName}.zip zip-application"
                }
            }
        }
        
        stage('Deploy to Apache') {
            steps {
                script {
                    sh "mkdir -p /var/www/html/${env.folderName}"
                    sh "unzip ${env.folderName}.zip -d /var/www/html/${env.folderName}"
                }
            }
        }
        
        stage('Start Application') {
            steps {
                script {
                    sh "cd /var/www/html/${env.folderName}"
                    sh "nohup python app.py &"
                }
            }
        }
        
        stage('Create Soft Link') {
            steps {
                script {
                    sh "ln -s /var/www/html/${env.folderName} /var/www/html/current"
                }
            }
        }
    }
}
