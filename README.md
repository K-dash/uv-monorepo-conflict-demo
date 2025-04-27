# uv-monorepo-conflict-demo

This repository demonstrates a dependency conflict scenario in a monorepo managed by `uv`.

## How to Reproduce the Conflict


1.  **Set up the virtual environment for the `common` package:**

    ```bash
    cd common
    uv venv && uv sync && uv pip install -e .
    ```

2.  **Attempt to set up the virtual environment for `repo_a` (this will trigger the conflict):**

    ```bash
    cd repo_a
    uv venv && uv sync && uv pip install -e .
    ```

3.  **Observe the error:**
    You should see an error message similar to this, indicating that `repo_a`'s requirement for `requests==2.31.0` conflicts with `common`'s requirement for `requests==2.32.1`:

    ```
      × No solution found when resolving dependencies:
      ╰─▶ Because only common==0.1.0 is available and common==0.1.0 depends on requests==2.32.1, we can conclude that all versions of common depend on requests==2.32.1.
          And because your project depends on common and requests==2.31.0, we can conclude that your project's requirements are unsatisfiable.
    ```
