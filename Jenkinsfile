pipeline {
    agent any
    
    stages {
        stage('Clone and Unzip') {
            steps {
                // Clone the repository as a zip file
                sh 'git clone --depth 1 https://github.com/Meenakshi0812/zip-application.git app.zip'
                
                // Generate folder name based on timestamp
                def folderName = sh(script: 'date +"%Y%m%d%H%M%S"', returnStdout: true).trim()
                
                // Unzip the code to www/var/html path
                sh "unzip -q app.zip -d /var/www/html/${folderName}"
            }
        }
        
        stage('Create Soft Link') {
            steps {
                // Create soft link for the pulled code
                sh "ln -s /var/www/html/${folderName} /var/www/html/current"
            }
        }
    }
}
