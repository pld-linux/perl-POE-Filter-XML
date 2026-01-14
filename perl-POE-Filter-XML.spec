#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	POE
%define		pnam	Filter-XML
Summary:	POE::Filter::XML - a POE Filter for parsing XML
Summary(pl.UTF-8):	POE::Filter::XML - filtr POE do analizy XML-a
Name:		perl-POE-Filter-XML
Version:	0.38
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	12a32a62f5da5131e2b40773e4b7cefc
URL:		http://search.cpan.org/dist/POE-Filter-XML/
BuildRequires:	perl-ExtUtils-AutoInstall >= 0.32
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Filter-Template
BuildRequires:	perl-POE >= 1:0.3401
BuildRequires:	perl-PXR
BuildRequires:	perl-XML-SAX >= 0.14
BuildRequires:	perl-XML-SAX-Expat
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Filter::XML provides POE with a completely encapsulated XML
parsing strategy for POE::Wheels that will be dealing with XML
streams.

POE::Filter::XML relies upon XML::SAX and XML::SAX::ParserFactory to
acquire a parser for parsing XML.

%description -l pl.UTF-8
POE::Filter::XML udostępnia POE z całkowicie obudowaną strategią
analizy XML-a dla POE::Wheels, obsługującą strumienie XML.

POE::Filter::XML polega na modułach XML::SAX i XML::SAX::ParserFactory
w celu uzyskania analizatora XML-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{perl_vendorlib}/POE/Filter/XML.pm
%{perl_vendorlib}/POE/Filter/XML
%{_mandir}/man3/*
