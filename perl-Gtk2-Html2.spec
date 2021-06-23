#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%define		pnam	Gtk2-Html2
Summary:	Gtk2::Html2 - Perl interface to gtkhtml2 library
Summary(pl.UTF-8):	Gtk2::Html2 - perlowy interfejs do biblioteki gtkhtml2
Name:		perl-Gtk2-Html2
Version:	0.06
Release:	1
License:	LGPL v2+
Group:		Development/Languages/Perl
Source0:	https://downloads.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	827b00137fcee6372cb7e07c9a3c0a9f
Patch0:		%{name}-build.patch
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	libgtkhtml-devel >= 2.0.0
BuildRequires:	perl-ExtUtils-Depends >= 0.200
BuildRequires:	perl-ExtUtils-PkgConfig >= 0.1
BuildRequires:	perl-Glib-devel >= 1.040
BuildRequires:	perl-Gtk2-devel >= 1.040
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Requires:	libgtkhtml >= 2.0.0
Requires:	perl-Glib >= 1.040
Requires:	perl-Gtk2 >= 1.040
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Gtk2::Html2 extension allows a Perl developer to use the gtkhtml2
HTML display widget with perl-Gtk2.

Note: this module is deprecated and no longer maintained.

%description -l pl.UTF-8
Moduł Gtk2::Html2 pozwala programistom perlowym używać widgetu
wyświetlającego HTML gtkhtml2 wraz z modułem perl-Gtk2.

Uwaga: ten moduł jest przestarzały i nie jest już utrzymywany.

%package devel
Summary:	Development files for Perl Gtk2-Html2 bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Gtk2-Html2 dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	libgtkhtml-devel >= 2.0.0
Requires:	perl-Cairo-devel
Requires:	perl-Glib-devel >= 1.040
Requires:	perl-Gtk2-devel >= 1.040

%description devel
Development files for Perl Gtk2-Html2 bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Gtk2-Html2 dla Perla.

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p1

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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Gtk2/Html2/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{perl_vendorarch}/Gtk2/Html2.pm
%dir %{perl_vendorarch}/Gtk2/Html2
%dir %{perl_vendorarch}/auto/Gtk2/Html2
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/Html2/Html2.so
%{_mandir}/man3/Gtk2::Html2*.3pm*

%files devel
%defattr(644,root,root,755)
%{perl_vendorarch}/Gtk2/Html2/Install
