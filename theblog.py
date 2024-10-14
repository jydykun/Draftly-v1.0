from app import create_app
from app.models import db, Category
import click
import subprocess

app = create_app()

# Command Line Interface for theblog web application
@click.group()
def cli():
    pass

# Command to run the application in debug mode
@cli.command()
def run_debug():
    app.run(debug=True)

# Initialiazed the database after defining the models
@cli.command()
def init_db():
    with app.app_context():
        db.create_all()
        click.echo("Database initialized.")

# Adding new category to the database
@cli.command()
@click.argument("key")
@click.argument("name")
def add_category(key, name):
    with app.app_context():
        # Create a category instance
        category = Category(key=key, name=name)
        db.session.add(category)
        db.session.commit()
        click.echo(f"Category '{key}:{name}' added successfully.")

# Run Tailwind in watch mode
@cli.command()
def run_tw():

    input = "./app/static/css/input.css"
    output = "./app/static/css/output.css"

    subprocess.run(["npx", "tailwind", "-i", input, "-o", output, "--watch"], shell=True, check=True)
    click.echo("Tailwind CSS is running with watch mode.")


if __name__ == "__main__":
    cli()