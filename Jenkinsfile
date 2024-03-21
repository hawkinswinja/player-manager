pipeline {
    agent {
        label 'pm-prod'
    }

    parameters {
        choice(choices:['updates','new', 'scale-web'], description: 'fkf build Choice', name: 'CHOICE')
    }

    environment {
        FKF_PASSWORD = credentials('fkf-user')
        FKF_ADMIN = credentials('fkf-passwd')
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
	stage('update') {
            when { 
                expression { env.CHOICE == 'tests' }
            }
	    steps {
                sh 'make crashed'
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
