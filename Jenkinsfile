pipeline {
    agent any
    environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'
    }
    stages {
        stage('Deploy') {
            steps {
                sh '''
                cp fkf.conf ~/nginx-conf
                ls ~/nginx-conf
                echo $DISABLE_AUTH $DB_ENGINE
                '''
            }
        }
        post {
            always {
                deleteDir() /* clean up our workspace */
                echo 'One way or another, I have finished'
            }
        }
    }
}
