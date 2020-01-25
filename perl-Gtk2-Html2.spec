#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%define		pnam	Gtk2-Html2
Summary:	Gtk2::Html2 - Perl interface to gtkhtml2 library
Summary(pl.UTF-8):	Gtk2::Html2 - perlowy interfejs do biblioteki gtkhtml2
Name:		perl-Gtk2-Html2
Version:	0.04
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	f6e9bc1d93c9de735f70801912855ded
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	libgtkhtml-devel >= 2.0.0
BuildRequires:	perl-ExtUtils-Depends >= 0.200
BuildRequires:	perl-ExtUtils-PkgConfig >= 0.1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Glib >= 1.040
BuildRequires:	perl-Gtk2 >= 1.040
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	libgtkhtml >= 2.0.0
Requires:	perl-Glib >= 1.040
Requires:	perl-Gtk2 >= 1.040
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gtk2::Html2 extension allows a Perl developer to use the gtkhtml2
HTML display widget with perl-Gtk2.

%description -l pl.UTF-8
Moduł Gtk2::Html2 pozwala programistom perlowym używać widgetu
wyświetlającego HTML gtkhtml2 wraz z modułem perl-Gtk2.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gtk2/Html2/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{perl_vendorarch}/Gtk2/Html2.pm
%dir %{perl_vendorarch}/Gtk2/Html2
%{perl_vendorarch}/Gtk2/Html2/Install
%dir %{perl_vendorarch}/auto/Gtk2/Html2
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/Html2/Html2.so
%{_mandir}/man3/Gtk2::Html2*.3pm*
