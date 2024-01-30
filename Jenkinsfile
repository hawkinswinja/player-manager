pipeline {
    agent any

    parameters {
        choice(choices:['updates','new'], description: 'fkf build Choice', name: 'CHOICE')
    }

    environment {
        FKF_PASSWD = credentials('fkf-user')
        FKF_USER = credentials('fkf-passwd')
    }
    stages {
        stage('Deploy') {
            when { 
                expression { env.CHOICE == 'new' }
            }
	    steps {
                sh 'make all'
            }
        }
        stage('Patch') {
            when { 
                expression { env.CHOICE == 'updates' }
            }
            steps {
                sh 'make stop_fkf'
                sh 'make fkf_run'
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
