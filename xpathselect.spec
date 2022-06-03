Name:           xpathselect
Version:	1.4.20140708
Release:	0
License:	GPL-3.0
Summary:	Select objects in an object tree using XPath queries
Url:	https://launchpad.net/xpathselect
Group:	System/Libraries
Source:	%{name}-%{version}.tar.xz
Patch:	xpathselect-no-test.patch
BuildRequires:	cmake
BuildRequires:	gcc-c++
BUildRequires:	pkg-config
BuildRequires:	boost-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%setup -q
%patch -p1

%build
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
make %{?_smp_mflags}

%install
cd build
%make_install
cd ..

%post -n libxpathselect1_4 -p /sbin/ldconfig

%postun -n libxpathselect1_4 -p /sbin/ldconfig

%files -n libxpathselect1_4
%defattr(-,root,root)
%doc debian/changelog COPYING
%{_libdir}/libxpathselect.so.1.4

%files devel
%defattr(-,root,root)
%{_includedir}/xpathselect
%{_libdir}/libxpathselect.so
%{_libdir}/pkgconfig/xpathselect.pc
