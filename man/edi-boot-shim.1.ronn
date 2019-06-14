edi-boot-shim(1) -- Embedded Development Infrastructure Boot Shim
=================================================================

## SYNOPSIS

`edi-boot-shim` <kernel-package-name>

## DESCRIPTION

Small utility that helps updating the u-boot boot configuration
without copying around initial ramdisks and kernels.

## OPTIONS

 * `-h`, `--help` :
   Displays the help screen.

## EXAMPLES

Instruct u-boot to boot the kernel contained in the given Debian
package on the next startup:

    $ edi-boot-shim linux-image-4.18.0-2-arm64

## COPYRIGHT

**edi and edi-boot-shim** is copyright (c) 2018, Matthias Luescher. Released
under the GNU Lesser General Public License.

## SEE ALSO

https://www.get-edi.io
