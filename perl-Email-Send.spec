%define upstream_name       Email-Send
%define upstream_version    2.196

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1
Summary:        Simply Sending Email
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{upstream_name}
Source:         http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.gz
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
%setup -q -n %{upstream_name}-%{upstream_version} 

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


