%define		appname	kernelupdatenotifier

Summary:	Kernel Update Notifier for KDE4
Summary(pl.UTF-8):	Powiadomienie o zaktualizowanym kernelu dla KDE4
Name:		kde4-%{appname}
Version:	1.1.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	%{appname}-%{version}.tar.gz
# Source0-md5:	908fd0a521b87b75168f020b648cdf03
BuildRequires:	cmake
BuildRequires:	kde4-kdebase-workspace-devel
BuildRequires:	kde4-kdelibs-devel
Suggests:	kernel-desktop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kernel Update Notifier for KDE4.

%description -l pl.UTF-8
Powiadomienie o zaktualizowanym kernelu dla KDE4.

%prep
%setup -q -n %{appname}-%{version}

%build
install -d build
cd build
%cmake \
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
