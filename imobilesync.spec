Summary:	A project for syncing iDevices using libimobiledevice
Name:		imobilesync
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Development/Languages/Python
Source0:	https://github.com/bryanforbes/imobilesync/tarball/master/%{name}.tgz
# Source0-md5:	5150e46b7df18d897b3e36c4f8edde99
URL:		https://github.com/bryanforbes/imobilesync/
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-imobiledevice
Requires:	python-vobject
Suggests:	conduit
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A package to provide synchronization capabilities for iDevices. Comes
with an optional Conduit module.

%prep
%setup -qc
mv *-imobilesync-*/* .

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/imobilesync
%dir %{py_sitescriptdir}/imobilesync
%{py_sitescriptdir}/imobilesync/*.py[co]
%dir %{py_sitescriptdir}/imobilesync/data
%{py_sitescriptdir}/imobilesync/data/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/imobilesync-*.egg-info
%endif
