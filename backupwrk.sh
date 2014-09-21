#!/bin/bash
p=$PWD;
cd ..;
tar cvf ./mediDbase.tar ./mediDbase;
gzip -f ./mediDbase.tar;
scp ./mediDbase.tar.gz nemo@nemor.cz:/raid/home/nemo/00_imp_data_rep_nemo/SKOLA2/UK-PYT;
cd $p;
