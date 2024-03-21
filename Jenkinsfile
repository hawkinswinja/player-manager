pipeline {
    agent {
        label 'pm-prod'
    }

    parameters {
        choice(choices:['updates','new'], description: 'fkf build Choice', name: 'CHOICE')
    }

    environment {
        FKF_AMIN = credentials('fkf-user')
        FKF_PASS = credentials('fkf-passwd')
        ALLOWED_HOSTS = credentials('allowed-hosts')
    }
    stages {
        stage ('Build') {
            steps {
                sh 'make build'
            }
        }
        
        stage ('Test') {
            steps {
                sh 'make test'
            }
        }
        
        stage('Push') {
	        steps {
                sh 'TAG=${env.BUILD_ID} make push'
            }
        }

        stage('Deploy') {
            when { 
                expression { env.CHOICE == 'deploy' }
            }
            steps {
                sh 'TAG=${env.BUILD_ID} DEBUG=0 SECRET_KEY=${FKF_PASS} ALLOWED_HOSTS=${ALLOWED_HOSTS} FKF_ADMIN=${FKF_ADMIN} FKF_PASSWORD=${FKF_PASS} make new_deploy'
            }
        }

        stage('Update') {
            when { 
                    expression { env.CHOICE == 'update' }
            }
            steps {
                    sh 'TAG=${env.BUILD_ID} DEBUG=0 SECRET_KEY=${FKF_PASS} ALLOWED_HOSTS=${ALLOWED_HOSTS} FKF_ADMIN=${FKF_ADMIN} FKF_PASSWORD=${FKF_PASS} make update'
            }
        }

    post {
        failure {
            echo 'notify job status as failure'
        }
        success {
            echo 'notify job status as success'
        }
        always {
            deleteDir() /* clean up our workspace */
            echo 'One way or another, I have finished'
        }
    }
}
