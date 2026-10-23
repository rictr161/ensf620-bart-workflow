# Scripts

This directory now includes `check_fourier_numpy.py` and `visualize_synthetic.py`,
imported from Ricardo's original synthetic run and present in the supplied staged
diff. The starter deliberately omitted them until the local copies were available;
they have not been replaced with newly generated numerical implementations.
Re-execution from this assembled repository remains pending.

Keep both together: visualization imports `read_bart_2d` from the checker. Its
`__main__` guard prevents intentionally rerunning reconstruction during import.
Both scripts read BART arrays from the current working directory. Invoke their
absolute paths while inside the intended synthetic run folder.

The reader is limited to the documented 64 × 64 fixture with trailing singleton
dimensions. Generic input handling and the automated BART workflow remain future
work. Do not copy laboratory extraction code into this directory.
