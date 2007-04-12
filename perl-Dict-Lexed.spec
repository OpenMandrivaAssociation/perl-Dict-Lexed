%define module	Dict-Lexed
%define name	perl-%{module}
%define version 0.2.2
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Lexed wrapper
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:		    http://search.cpan.org/CPAN/authors/id/G/GR/GROUSSE/%{module}-%{version}.tar.bz2
Requires:	    lexed
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	lexed
Buildarch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
This module is a perl wrapper around Lexed, a lexicalizer developed at INRIA.

%prep
%setup -q -n %{module}-%{version}

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
%doc README ChangeLog
%{perl_vendorlib}/Dict
%{_mandir}/*/*

