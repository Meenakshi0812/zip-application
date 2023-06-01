pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Meenakshi0812/zip-application.git'
            }
        }
        
        stage('Deploy to Apache') {
            steps {
                script {
                    def folderName = sh(script: 'date +"%Y%m%d%H%M%S"', returnStdout: true).trim()
                    sh "mv zip-application/app.py /var/www/html/${folderName}"
                }
            }
        }
        
        stage('Create Soft Link') {
            steps {
                sh 'ln -s /var/www/html/${folderName} /var/www/html/latest'
            }
        }
    }
}
