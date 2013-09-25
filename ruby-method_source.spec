#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	method_source
Summary:	Retrieve the source code for a method
Name:		ruby-%{pkgname}
Version:	0.8.1
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	-
URL:		http://banisterfiend.wordpress.com/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-bacon < 1.2
BuildRequires:	ruby-bacon >= 1.1.0
BuildRequires:	ruby-rake < 1
BuildRequires:	ruby-rake >= 0.9
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Retrieve the sourcecode for a method.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
%setup -q -n %{pkgname}-%{version}

%build
%if %{with tests}
bacon test/test.rb
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.markdown LICENSE
%{ruby_vendorlibdir}/method_source.rb
%{ruby_vendorlibdir}/method_source
