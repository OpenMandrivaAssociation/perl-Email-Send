%define upstream_name       Email-Send
%define upstream_version 2.199

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Simply Sending Email
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Email/Email-Send-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Capture::Tiny)
BuildRequires:	perl(Email::Simple)
BuildRequires:	perl(Email::Address)
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(Return::Value)
Requires:	perl(Email::Date::Format)

BuildArch:	noarch

%description
This module provides a very simple, very clean, very specific interface to
multiple Email mailers. The goal of this software is to be small and simple,
easy to use, and easy to extend.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*


%changelog
* Tue Dec 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.198.0-2mdv2010.1
+ Revision: 472190
- adding a requires:

* Thu Jul 16 2009 Jérôme Quelin <jquelin@mandriva.org> 2.198.0-1mdv2010.0
+ Revision: 396578
- update to 2.198

* Wed Jul 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.197.0-1mdv2010.0
+ Revision: 393522
- update to new version 2.197

* Wed Jun 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.196.0-1mdv2010.0
+ Revision: 384798
- new version

* Wed Feb 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.194.0-1mdv2010.0
+ Revision: 337653
- new release
- standardized version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.19.2-3mdv2009.0
+ Revision: 256788
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.19.2-1mdv2008.1
+ Revision: 109609
- new version (upstream version 2.192)


* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.18.5-1mdv2007.1
+ Revision: 138834
- new version

* Sun Jan 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.18.3-1mdv2007.1
+ Revision: 111237
- fix build dependencies
- fix build dependencies
- Import perl-Email-Send

* Sat Jan 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.18.3-1mdv2007.1
- first mdv release


