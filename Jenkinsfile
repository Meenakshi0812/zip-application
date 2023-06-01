pipeline {
    agent any
    
    stages {
        stage('Clean Workspace') {
            steps {
                sh 'rm -rf zip-application'
            }
        }
        
        stage('Clone Repository') {
            steps {
                sh 'git clone --depth 1 https://github.com/Meenakshi0812/zip-application.git zip-application'
            }
        }
        
        stage('Create Zip') {
            steps {
                script {
                    def folderName = sh(script: 'date +"%Y%m%d%H%M%S"', returnStdout: true).trim()
                    sh "tar -czf ${folderName}.tar.gz zip-application"
                }
            }
        }
        
        stage('Deploy to Apache') {
            steps {
                script {
                    def folderName = sh(script: 'date +"%Y%m%d%H%M%S"', returnStdout: true).trim()
                    sh "mkdir -p /var/www/html/${folderName}"
                    sh "tar -xzf ${folderName}.tar.gz -C /var/www/html/${folderName}"
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
