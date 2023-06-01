pipeline {
    agent any
    
    stages {
        stage('Clean Workspace') {
            steps {
                sh 'rm -rf zip-application'
            }
        }
        
        stage('Clone Repository as Zip') {
            steps {
                script {
                    def folderName = sh(script: 'date +"%Y%m%d%H%M%S"', returnStdout: true).trim()
                    sh 'git clone --depth 1 https://github.com/Meenakshi0812/zip-application.git zip-application'
                    sh "zip -r ${folderName}.zip zip-application"
                }
            }
        }
        
        stage('Deploy to Apache') {
            steps {
                script {
                    def folderName = sh(script: 'date +"%Y%m%d%H%M%S"', returnStdout: true).trim()
                    sh "mkdir -p /var/www/html/${folderName}"
                    sh "unzip ${folderName}.zip -d /var/www/html/${folderName}"
                }
            }
        }
        
        stage('Create Soft Link') {
            steps {
                script {
                    def folderName = sh(script: 'date +"%Y%m%d%H%M%S"', returnStdout: true).trim()
                    sh "ln -s /var/www/html/${folderName} /var/www/html/current"
                }
            }
        }
    }
}
