# almalinux-git-utils

Utilities for working with the AlmaLinux OS Git server.


## alma_get_sources

The `alma_get_sources` script downloads sources and BLOBs from the AlmaLinux
sources cache.

### Usage

Run the `alma_get_sources` in a git project root directory:

1. Clone an AlmaLinux RPM package git project from
   [git.almalinux.org](https://git.almalinux.org).
2. Switch to a required branch.
3. Run the `alma_get_sources` tool:
   ```shell
   $ alma_get_sources
   ```


## alma_blob_upload

The `alma_blob_upload` script uploads sources and BLOBs to the AlmaLinux
sources cache.

### Prerequirements

Create an AWS credentials file ~/.aws/credentials with the following content:

```ini
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```


### Usage

The utility supports two types of input: a CentOS git repository metadata file
or a list of files to upload.

For CentOS repositories workflow will be the following:

1. Install the `get_sources.sh` script from the
   [centos-git-common](https://git.centos.org/centos-git-common) repository.
2. Clone a project and download its sources as described on the CentOS
   [Wiki](https://wiki.centos.org/Sources).
3. Run the `alma_blob_upload` tool (don't forget to replace `PROJECT_NAME` with
   an actual project name):
   ```shell
   $ alma_blob_upload -i .PROJECT_NAME.metadata
   ```

Alternatively, you can upload a list of files in the following way:

```shell
$ alma_blob_upload -f SOURCES/FILE_1 SOURCES/FILE_N
```

The `alma_blob_upload` utility can also generate a CentOS-compatible metadata
file:

```shell
$ alma_blob_upload -o .PROJECT_NAME.metadata -f SOURCES/FILE_1 SOURCES/FILE_N
```


## License

Licensed under the GPLv3 license, see the LICENSE file for details.
