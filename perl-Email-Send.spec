%define module      Email-Send
%define name        perl-%{module}
%define version     2.19.2
%define up_version  2.192
%define release     %mkrel 3

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Simply Sending Email
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Email/%{module}-%{up_version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Return::Value)
BuildRequires:  perl(Email::Simple)
BuildRequires:  perl(Email::Address)
BuildRequires:  perl(Module::Pluggable)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module provides a very simple, very clean, very specific interface to
multiple Email mailers. The goal of this software is to be small and simple,
easy to use, and easy to extend.

%prep
%setup -q -n %{module}-%{up_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*


