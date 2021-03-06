Summary:	XCB support libraries
Name:		xcb-util
Version:	0.4.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	2e97feed81919465a04ccc71e4073313
URL:		http://xcb.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gperf
BuildRequires:	libtool
BuildRequires:	libxcb-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package devel
Summary:	Header files for XCB util libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for XCB util libraries.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %ghost %{_libdir}/libxcb-*.so.1
%attr(755,root,root) %{_libdir}/libxcb-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-*.so
%{_includedir}/xcb/xcb_*.h
%{_pkgconfigdir}/xcb-*.pc

