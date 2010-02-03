%define		orgname	kernelupdatenotifier
%define		qtver	4.5.3
%define		kdever	4.3.5

Summary:	Kernel Update Notifier for KDE4
Summary(pl.UTF-8):	Powiadomienie o zaktualizowanym kernelu dla KDE4
Name:		kde4-%{orgname}
Version:	1.1.2
Release:	3
License:	GPL v2+
Group:		X11/Applications
Source0:	%{orgname}-%{version}.tar.gz
# Source0-md5:	87f53d06444ada673a176e5cadfe9c2c
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.6.3
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
Suggests:	kernel-desktop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kernel Update Notifier for KDE4.

%description -l pl.UTF-8
Powiadomienie o zaktualizowanym kernelu dla KDE4.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	../

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/apps/kernelupdatenotifier
install *.notifyrc $RPM_BUILD_ROOT%{_datadir}/apps/kernelupdatenotifier

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kernelupdatenotifier
%{_datadir}/apps/kernelupdatenotifier
