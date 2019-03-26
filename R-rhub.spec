#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rhub
Version  : 1.1.0
Release  : 2
URL      : https://cran.r-project.org/src/contrib/rhub_1.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rhub_1.1.0.tar.gz
Summary  : Connect to 'R-hub'
Group    : Development/Tools
License  : MIT
Requires: R-backports
Requires: R-callr
Requires: R-desc
Requires: R-parsedate
Requires: R-pillar
Requires: R-pkgbuild
Requires: R-prettyunits
Requires: R-ps
Requires: R-rappdirs
Requires: R-rcmdcheck
Requires: R-rematch
Requires: R-rprojroot
Requires: R-tibble
Requires: R-uuid
Requires: R-whoami
Requires: R-xopen
BuildRequires : R-backports
BuildRequires : R-callr
BuildRequires : R-desc
BuildRequires : R-parsedate
BuildRequires : R-pillar
BuildRequires : R-pkgbuild
BuildRequires : R-prettyunits
BuildRequires : R-ps
BuildRequires : R-rappdirs
BuildRequires : R-rcmdcheck
BuildRequires : R-rematch
BuildRequires : R-rprojroot
BuildRequires : R-tibble
BuildRequires : R-uuid
BuildRequires : R-whoami
BuildRequires : R-xopen
BuildRequires : buildreq-R

%description
architectures, from the command line. The current architectures include
    'Windows', 'macOS', 'Solaris' and various 'Linux' distributions.

%prep
%setup -q -c -n rhub

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1553619997

%install
export SOURCE_DATE_EPOCH=1553619997
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rhub
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rhub
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rhub
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  rhub || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rhub/DESCRIPTION
/usr/lib64/R/library/rhub/INDEX
/usr/lib64/R/library/rhub/LICENSE
/usr/lib64/R/library/rhub/Meta/Rd.rds
/usr/lib64/R/library/rhub/Meta/features.rds
/usr/lib64/R/library/rhub/Meta/hsearch.rds
/usr/lib64/R/library/rhub/Meta/links.rds
/usr/lib64/R/library/rhub/Meta/nsInfo.rds
/usr/lib64/R/library/rhub/Meta/package.rds
/usr/lib64/R/library/rhub/Meta/vignette.rds
/usr/lib64/R/library/rhub/NAMESPACE
/usr/lib64/R/library/rhub/NEWS.md
/usr/lib64/R/library/rhub/R/rhub
/usr/lib64/R/library/rhub/R/rhub.rdb
/usr/lib64/R/library/rhub/R/rhub.rdx
/usr/lib64/R/library/rhub/bin/rhub-linux-docker.sh
/usr/lib64/R/library/rhub/bin/rhub-linux.sh
/usr/lib64/R/library/rhub/doc/index.html
/usr/lib64/R/library/rhub/doc/local-debugging.R
/usr/lib64/R/library/rhub/doc/local-debugging.Rmd
/usr/lib64/R/library/rhub/doc/local-debugging.html
/usr/lib64/R/library/rhub/doc/rhub.R
/usr/lib64/R/library/rhub/doc/rhub.Rmd
/usr/lib64/R/library/rhub/doc/rhub.html
/usr/lib64/R/library/rhub/help/AnIndex
/usr/lib64/R/library/rhub/help/aliases.rds
/usr/lib64/R/library/rhub/help/figures/logo.png
/usr/lib64/R/library/rhub/help/paths.rds
/usr/lib64/R/library/rhub/help/rhub.rdb
/usr/lib64/R/library/rhub/help/rhub.rdx
/usr/lib64/R/library/rhub/html/00Index.html
/usr/lib64/R/library/rhub/html/R.css
/usr/lib64/R/library/rhub/tests/testthat.R
/usr/lib64/R/library/rhub/tests/testthat/helpers.R
/usr/lib64/R/library/rhub/tests/testthat/test-api.R
/usr/lib64/R/library/rhub/tests/testthat/test-assertions.R
/usr/lib64/R/library/rhub/tests/testthat/test-build.R
/usr/lib64/R/library/rhub/tests/testthat/test-check.R
/usr/lib64/R/library/rhub/tests/testthat/test-email.R
/usr/lib64/R/library/rhub/tests/testthat/test-error.R
/usr/lib64/R/library/rhub/tests/testthat/test-platforms.R
/usr/lib64/R/library/rhub/tests/testthat/test-print.R
/usr/lib64/R/library/rhub/tests/testthat/test-submit.R
/usr/lib64/R/library/rhub/tests/testthat/test-utils.R
