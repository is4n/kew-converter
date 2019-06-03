# install PDFminer.six
pip3 install pdfminer.six

# make sure scripts are executable
chmod +x kew_converter.sh
chmod +x scripts/get_lsn_index.sh

# download and build SWFtools
wget http://swftools.org/swftools-0.9.2.tar.gz
gzip -d swftools-0.9.2.tar.gz
tar -xf swftools-0.9.2.tar
rm swftools-0.9.2.tar

cd swftools-0.9.2
./configure
make
cd ..
mv swftools-0.9.2 lib/swftools
