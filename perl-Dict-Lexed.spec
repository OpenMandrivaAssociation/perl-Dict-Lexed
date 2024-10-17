%define module	Dict-Lexed

Name:		perl-%{module}
Version:	0.2.2
Release:	9
Summary:	Lexed wrapper
License:	GPL or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/authors/id/G/GR/GROUSSE/%{module}-%{version}.tar.bz2
Requires:	lexed
BuildRequires:	perl-devel
BuildRequires:	lexed
BuildArch:	noarch

%description
This module is a perl wrapper around Lexed, a lexicalizer developed at INRIA.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc README ChangeLog
%{perl_vendorlib}/Dict
%{_mandir}/*/*

%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.2.2-6mdv2011.0
+ Revision: 681412
- mass rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2.2-5mdv2011.0
+ Revision: 430412
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.2.2-4mdv2009.0
+ Revision: 256678
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.2.2-2mdv2008.1
+ Revision: 135833
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.2-2mdv2008.0
+ Revision: 86354
- rebuild


* Tue Sep 05 2006 guillomovitch
+ 2006-09-05 09:03:27 (59950)
new version

* Thu Aug 03 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org>
+ 2006-08-03 13:00:59 (43208)
import perl-Dict-Lexed-0.2.1-5mdk

* Sun Nov 06 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.1-5mdk
- clean up buildrequires

* Mon Oct 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.1-4mdk
- Fix previous mistake

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.1-3mdk
- Fix BuildRequires

* Mon Jun 13 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.1-2mdk 
- first mdk release

