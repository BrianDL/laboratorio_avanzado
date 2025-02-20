{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/basics/
  # env.GREET = "devenv";

  # https://devenv.sh/packages/
  packages = with pkgs; [
    git entr findutils
  ];

  # https://devenv.sh/languages/
  languages.texlive = {
    enable = true;
    packages = with pkgs.texlive;
      [ "babel-spanish" ];
  };

  # https://devenv.sh/processes/
  # processes.cargo-watch.exec = "cargo-watch";

  # https://devenv.sh/services/
  # services.postgres.enable = true;

  # https://devenv.sh/scripts/
    scripts.watch-latex.exec = ''
      #!/usr/bin/env bash
      if [ $# -eq 0 ]; then
        echo "Usage: $0 <project-directory>"
        exit 1
      fi

      PROJECT_DIR="$1"
      MAIN_TEX="$PROJECT_DIR/main.tex"
      MAIN_NAME=$(basename "$MAIN_TEX" .tex)

      if [ ! -f "$MAIN_TEX" ]; then
        echo "Error: main.tex not found in $PROJECT_DIR"
        exit 1
      fi

      echo "Watching LaTeX files in $PROJECT_DIR..."
      find "$PROJECT_DIR" -name "*.tex" -or -name "*.bib" | entr -s "cd $PROJECT_DIR && pdflatex -interaction=nonstopmode $MAIN_NAME && bibtex $MAIN_NAME && pdflatex -interaction=nonstopmode $MAIN_NAME && pdflatex -interaction=nonstopmode $MAIN_NAME && echo 'Compilation completed.'"
    '';

  # https://devenv.sh/tasks/
  # tasks = {
  #   "myproj:setup".exec = "mytool build";
  #   "devenv:enterShell".after = [ "myproj:setup" ];
  # };

  # https://devenv.sh/tests/
  enterTest = ''
    echo "Running tests"
    git --version | grep --color=auto "${pkgs.git.version}"
  '';

  # https://devenv.sh/pre-commit-hooks/
  # pre-commit.hooks.shellcheck.enable = true;

  # See full reference at https://devenv.sh/reference/options/
}
