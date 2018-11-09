ext4load mmc 0:2 ${kernel_addr_r} /boot/vmlinuz-__KERNEL_PACKAGE_VERSION__
ext4load mmc 0:2 ${fdt_addr_r} /usr/lib/linux-image-__KERNEL_PACKAGE_VERSION__/${fdtfile}
ext4load mmc 0:2 ${ramdisk_addr_r} /boot/initrd.img-__KERNEL_PACKAGE_VERSION__

setenv bootargs console=tty0 console=ttyS1,115200 root=/dev/mmcblk0p2 rw elevator=deadline fsck.repair=yes net.ifnames=0 cma=128M rootwait

booti ${kernel_addr_r} ${ramdisk_addr_r}:${filesize} ${fdt_addr_r}