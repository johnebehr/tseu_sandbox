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
- Base app structure
  - ```shell
    .
    ├── LICENSE
    ├── README.md
    └── app
        ├── __init__.py
        ├── main.py
        └── util
            ├── __init__.py
            └── settings.py
    
    2 directories, 6 files
    ```
    - In <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">app.util.settings</span>, work ahead and add settings for the database connections that will be set up next.

### Database Support
- Refactor the app and start adding database support 
  - Add a new directory as a home for the database support 
  - Add <span style="font: 1.3rem Inconsolata, monospace; font-size:1.10em;">app.db.database</span> to handle database connection activities
  - Add a new directory for the database models which are reflected from the existing MySQL database.
  - Add a loader to centralize access to the models.connections
- Current app structure: 
  - ```shell
    .
    ├── LICENSE
    ├── README.md
    └── app
        ├── __init__.py
        ├── db
        │   ├── __init__.py
        │   ├── database.py
        │   ├── model_loader.py
        │   └── models
        │       ├── __init__py
        │       ├── cope_contributions.py
        │       ├── dues.py
        │       ├── dues_and_cope_track_2yrs.py
        │       ├── mast_agency.py
        │       ├── mast_city.py
        │       ├── mast_county.py
        │       ├── mast_location.py
        │       ├── mast_organizer.py
        │       └── members.py
        ├── main.py
        └── util
            ├── __init__.py
            └── settings.py

    4 directories, 19 files
    ```
### Search Member Routes
- Create an API route that will return a member by supplying a Social Security Number
  - Add a CRUD definition to query the Member database for member info by SSNo
  - Add a GET route that will return Member info
  - Add a Pydantic schema that will validate the return data for documentation.
  
