import typer
from core import rubik

app = typer.Typer(add_completion=False)


@app.command()
def run(
    cube_size: int = typer.Option(3, '--cube-size', '-s', help='Size of the Rubik Cube')
):
    cube = rubik.RubikCube(cube_size=cube_size)
    cube.gen_random()
    print(cube)


if __name__ == "__main__":
    app()
