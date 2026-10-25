# imported to execute the external 'maptoposter' CLI
import os
import subprocess


def build_leeds_map():
    """Render 17 different theme variations for Leeds using the map poster CLI tool."""

    print("🚀 Initializing Leeds Map Project...")

    # The 17 official internal theme style keys
    designs = [
        {"theme": "terracotta"},
        {"theme": "noir"},
        {"theme": "midnight_blue"},
        {"theme": "blueprint"},
        {"theme": "neon_cyberpunk"},
        {"theme": "warm_beige"},
        {"theme": "pastel_dream"},
        {"theme": "japanese_ink"},
        {"theme": "emerald"},
        {"theme": "forest"},
        {"theme": "ocean"},
        {"theme": "sunset"},
        {"theme": "autumn"},
        {"theme": "copper_patina"},
        {"theme": "monochrome_blue"},
        {"theme": "gradient_roads"},
        {"theme": "contrast_zones"}
    ]

    # Target the exact compiled Windows executable inside the virtual environment
    exe_path = os.path.abspath(r".venv\Scripts\maptoposter-cli.exe")

    # Loop through all 17 design configurations
    for design in designs:
        print(f"🗺️ Rendering theme ..[{design['theme'].upper()}]for Leeds...")

        # Build the literal command line arguments
        cli = [
            exe_path,
            "--city", "Leeds",
            "--country", "England",
            "--theme", 
            design['theme'],
            "--distance", 
            "10000" # Distance from above - aerial viewpoint
        ]

        try:
            # Run the exact file natively
            subprocess.run(
                cli, 
                check=True,
                timeout=300, # 5min safety limit
            )

            print(f" Theme [{design['theme'].upper()}] finished.")
        
        except subprocess.CalledProcessError as exc:
            print(
                f" Theme [{design['theme'].upper()}] "
                f"Failed with exit code {exc.returncode}."
            )

    # Rendering complete - print to console
    print("\n ✅ Complete! All designs are in the posters folder!")


if __name__ == "__main__":
    build_leeds_map()