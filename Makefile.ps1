
function asset-dist {
    $assetsFolderPath = ".\dist\app\_internal\assets"

    # Check if 'assets' folder exists, and create it if not
    if (-not (Test-Path -Path $assetsFolderPath -PathType Container)) {
        New-Item -Path $assetsFolderPath -ItemType Directory
    }

    Copy-Item -Path .\Rob.woff -Destination .\dist\app\_internal\assets
    Copy-Item -Path .\Rob.woff2 -Destination .\dist\app\_internal\assets
    Copy-Item -Path .\words_alpha.sqlite -Destination .\dist\app\_internal\assets
    Copy-Item -Path .\index.html -Destination .\dist\app\_internal\assets
    Copy-Item -Path .\detonary_favicon.ico -Destination .\dist\app\_internal\assets
}

function change-name {
    Rename-Item -Path .\dist\app\app.exe -NewName "detonary.exe"
}

function py-install {
    # Run pyinstaller to create an executable without console window
    pyinstaller --noconsole --icon=detonary_favicon.ico app.py
}

function py-install-debug {
    # Run pyinstaller to create an executable without console window
    pyinstaller app.py
}

function build {
    py-install
    asset-dist
    change-name
}

function build-debug {
    py-install-debug
    asset-dist
}