pipeline {
    agent any
    environment {
        FKF_PASSWD = credentials('fkf-user')
        FKF_USER = credentials('fkf-passwd')
    }
    stages {
        stage('Deploy') {
            steps {
                sh 'make set_nginx'
            }
        }
    }
    post {
        always {
            deleteDir() /* clean up our workspace */
            echo 'One way or another, I have finished'
        }
    }
}
