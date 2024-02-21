from pyngrok import ngrok

# Replace 'token' with your actual ngrok auth token
ngrok.set_auth_token('token')

def expose_local_port(port):
    # Expose the specified local TCP port as a public URL
    public_url = ngrok.connect(port, "tcp")
    print(f"Port {port} is now publicly accessible at {public_url}")

if __name__ == "__main__":
    try:
        # Prompt the user to enter a local TCP port
        local_port = int(input("Enter the local TCP port you want to make public: "))
        expose_local_port(local_port)
        
        # Keep the tunnel open until the user decides to stop the program
        input("Press Enter to stop the tunnel...")
    except ValueError:
        print("Please enter a valid port number.")
    finally:
        # When done, close all ngrok tunnels
        ngrok.disconnect_all()