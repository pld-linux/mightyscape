Summary:	Extension collection for Inkscape 1.0+
Name:		mightyscape
%define		snap	20210605
Version:	1.X.%{snap}
Release:	1
License:	GPL v3
Group:		Applications
Source0:	https://github.com/vmario89/mightyscape-1.X/archive/master/%{name}-%{version}.tar.gz
# Source0-md5:	621e44e8685eb51c6b89e01ca01d7085
URL:		https://y.stadtfabrikanten.org/mightyscape-doku
Requires:	inkscape
Requires:	python3-lxml
Requires:	python3-networkx
Requires:	python3-numpy
Requires:	python3-opencv
Requires:	python3-pillow
Requires:	python3-scipy
Requires:	python3-shapely
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
A maintained extension collection for Inkscape 1.0+.

%prep
%setup -q -n mightyscape-1.X-master
cd extensions/fablabchemnitz

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python3(\s|$),#!%{__python3}\1,' \
      */*.py

# Remove binary blobs and blob wrapper plugins
%{__rm} -r dxf2papercraft \
	papercraft_unfold \
	svg2shenzhen \
	primitive \
	cutting_optimizer \
	imagetracerjs \
	inkstitch \
	sudoku \
	svgo_output \
	boxes.py/boxes.exe \
	dxf_dwg_importer/{node.exe,node_modules,kabeja}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/inkscape/extensions

cp -ap extensions/fablabchemnitz $RPM_BUILD_ROOT%{_datadir}/inkscape/extensions/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{_datadir}/inkscape/extensions/fablabchemnitz
