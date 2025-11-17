import paramiko
import os
import logging
from fastapi import APIRouter, Query
from dotenv import load_dotenv

# Initialize the FastAPI router
router = APIRouter()

# Load environment variables
load_dotenv()

# Set up logging for debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.get("/trigger-topology")
def trigger_mininet(topo: str = Query(default="single,2")):
    """
    Trigger Mininet with a given topology string.
    Example: /trigger-topology?topo=tree,2
    """
    # Load environment variables
    ec2_ip = os.getenv("EC2_IP")
    user_name = os.getenv("EC2_USERNAME")
    key_path = os.getenv("KEY_PATH", "E:/Project/anil-key.pem")

    # Log the environment variables for debugging
    logger.info(f"EC2_IP: {ec2_ip}, USERNAME: {user_name}, KEY_PATH: {key_path}")

    try:
        # Load the private key
        logger.info("Loading private key...")
        private_key = paramiko.RSAKey.from_private_key_file(key_path)
        logger.info("Private key loaded successfully.")

        # Set up the SSH client
        logger.info("Setting up SSH client...")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        logger.info("Connecting to EC2 instance...")
        ssh.connect(hostname=ec2_ip, username=user_name, pkey=private_key)
        logger.info("SSH connection established.")

        # Dynamic Mininet command
        command = f"sudo mn --topo {topo} --controller=remote,ip=127.0.0.1,port=6653 --test pingall"
        logger.info(f"Executing command: {command}")
        _, stdout, stderr = ssh.exec_command(command)

        # Read the output and errors
        output = stdout.read().decode()
        error = stderr.read().decode()
        logger.info("Command executed successfully.")
        logger.info(f"Command output: {output}")
        logger.info(f"Command error: {error}")

        # Close the SSH connection
        ssh.close()
        logger.info("SSH connection closed.")

        # Return the response
        return {
            "status": "success",
            "topology": topo,
            "output": output,
            "error": error
        }

    except paramiko.AuthenticationException as auth_err:
        logger.error(f"Authentication failed: {auth_err}")
        return {
            "status": "error",
            "message": f"Authentication failed: {auth_err}"
        }
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return {
            "status": "error",
            "message": str(e)
        }
