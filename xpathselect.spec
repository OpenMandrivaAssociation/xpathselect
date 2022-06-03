Name:           xpathselect
Version:	1.4
Release:	1
License:	GPL-3.0
Summary:	Select objects in an object tree using XPath queries
Url:	https://launchpad.net/xpathselect
Group:	System/Libraries
Source:	https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/xpathselect/1.4+15.10.20150824.1-0ubuntu2/xpathselect_1.4+15.10.20150824.1.orig.tar.gz
#Patch:	xpathselect-no-test.patch
BuildRequires:	cmake
BuildRequires:	boost-devel

%description
This library allows you to select arbitrary objects in an object tree using a
small subset of the XPath specification.

%package -n libxpathselect1_4
Summary:	Select objects in an object tree using XPath queries
Group:	System/Libraries

%description -n libxpathselect1_4
This library allows you to select arbitrary objects in an object tree using a
small subset of the XPath specification.

%package devel
Summary:	Select objects in an object tree using XPath queries - development files
Group:	Development/Libraries/C and C++
Requires:	libxpathselect1_4 = %{version}

%description devel
This library allows you to select arbitrary objects in an object tree using a
small subset of the XPath specification.

This package contains development files for xpathselect.


%prep
%autosetup -n xpathselect-1.4+15.10.20150824.1 -p1

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix}
%make_build

%install
%make_install -C build

%files -n libxpathselect1_4
%defattr(-,root,root)
%doc debian/changelog COPYING
%{_libdir}/libxpathselect.so.1.4

%files devel
%defattr(-,root,root)
%{_includedir}/xpathselect
%{_libdir}/libxpathselect.so
%{_libdir}/pkgconfig/xpathselect.pc
