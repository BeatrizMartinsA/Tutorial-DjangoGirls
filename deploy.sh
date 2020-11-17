rsync -av --exclude .venv --exclude .idea --exclude dbdata ./* busercamp@evolutio.io:./bia/
ssh busercamp@evolutio.io bia/dkprod.sh