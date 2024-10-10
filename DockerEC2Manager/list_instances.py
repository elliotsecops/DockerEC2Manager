import os
import sys
import subprocess

def list_ec2_instances(region):
    try:
        # Usar variables de entorno para las credenciales AWS
        my_env = os.environ.copy()

        result = subprocess.run(
            ["aws", "ec2", "describe-instances", "--region", region],
            capture_output=True, text=True, env=my_env
        )

        if result.returncode == 0:
            print("EC2 Instances:")
            print(result.stdout)
        else:
            print(f"Error: {result.stderr}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Obtener la región desde los argumentos o usar us-east-1 como valor por defecto
    region = sys.argv[1] if len(sys.argv) > 1 else "us-east-1"
    list_ec2_instances(region)