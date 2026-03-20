#
# Conditional build:
%bcond_without	tests		# build without tests

%define	pkgname	method_source
Summary:	Retrieve the source code for a method
Name:		ruby-%{pkgname}
Version:	1.1.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	a8553bc1e3941e781683779da71d3896
Patch0:		ruby-3.4.patch
Patch1:		ruby-3.4-tests.patch
URL:		http://github.com/banister/method_source
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	rubygem(rspec)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Retrieve the source code for a method.

%prep
%setup -q -n %{pkgname}-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%__gem_helper spec

%if %{with tests}
rspec spec
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE CHANGELOG.md README.markdown
%{ruby_vendorlibdir}/method_source.rb
%{ruby_vendorlibdir}/method_source
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
