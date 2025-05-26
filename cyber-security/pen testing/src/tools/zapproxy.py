import os, subprocess
from crewai.tools import tool


@tool("ZapProxyGeneralUse")
def zap_general_use(website: str) -> str:
    """ Penn Testing on Web using ZapProxy Tool
    Parameters: website
    Returns:
    - str: The results of the ZAP operation or an error message.
    """
    base_command = f"java -Xmx1024m -jar zap-2.16.1.jar -quickurl {website} -quickprogress -cmd"
    print(f"Running ZapProzy command: {base_command}")
    return load_text_file("C:\\develop\gen_ai\\libraries\crewai\\pen_test_cyber_agent\\2025-04-27-ZAP-Report-.txt")
    # os.chdir(r"C:\Program Files\ZAP\Zed Attack Proxy")
    #
    #
    # process = subprocess.Popen(base_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #
    # stdout, stderr = process.communicate()
    #
    # if process.returncode != 0:
    #     print(stderr.decode('utf-8'))
    # raise Exception(f"Error executing ZAP: {stderr.decode('utf-8')}")

    # return stdout.decode("utf-8")

def load_text_file(file_path):
    """
    Loads a text file and returns its content as a string.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The content of the text file, or None if an error occurs.
    """
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        return None
    except Exception as e:
         print(f"An error occurred: {e}")
         return None

