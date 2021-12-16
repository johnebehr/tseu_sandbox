<div style="text-align:center">
<h1>TSEU FastAPI Sandbox</h1>
<h2>FastAPI Sandbox for testing App Ideas</h2>
</div>
<hr style="border: 3px solid #393e46; width:70%; margin:0 auto;">

### Resources
- Generating a random hex string for seeding purposes
    - ```shell
      $ # Use OpenSSL to generate a random 32-bit sting
      $ openssl rand -hex 32
      ```

### Setting Up
- Create a <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">main.py</span> file and make sure that FastAPI works
    - ```shell
      $ # Launch FastAPI manually this time
      $ python -m uvicorn main:app --host 0.0.0.0 --port 8000 --workers 1 --reload
      ```
- With the initial route up and going, perform the initial commit, bring down the container and add a command stanza to <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">docker-compose.yml</span>
  - ```yml
    version: '3.8' 
    
    services: 
      # FastAPI
      api:
        container_name: tseu-sandbox
        image: tseu-sandbox:base 
        build: 
          context: ./sandbox-container 
          # Bring up the Python base image 
          # target: base 
          # Bring up the Python Dev image layer
          target: dev 
        volumes:
          - ./sandbox-container/tseu_sandbox:/usr/src
        ports:
          - 8000:8000
        networks: 
          - tseu-sandbox-app 
        command: bash -c "python -m uvicorn main:app --host 0.0.0.0 --port 8000 --workers 1 --reload"
    
    networks:
      tseu-sandbox-app:
        driver: bridge
    ```