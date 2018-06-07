QEMU_VERSION=2.12.0
mkdir -p $HOME/Downloads/QEMU
cd $HOME/Downloads/QEMU
wget https://download.qemu.org/qemu-$QEMU_VERSION.tar.xz
tar xvJf qemu-$QEMU_VERSION.tar.xz
cd qemu-$QEMU_VERSION
./configure --target-list=arm-softmmu
make -j
sudo cp arm-softmmu/qemu-system-arm /usr/local/bin/
