%define		appname	kernelupdatenotifier
Summary:	Kernel Update Notifier for KDE4
Summary(pl.UTF-8):	Powiadomienie o zaktualizowanym kernelu dla KDE4
Name:		kde4-%{appname}
Version:	1.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	%{appname}-%{version}.tar.gz
# Source0-md5:	893c98029d54ed7417e1301774460733
BuildRequires:	kde4-kdebase-workspace-devel
BuildRequires:	kde4-kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kernel Update Notifier for KDE4.

%description -l pl.UTF-8
Powiadomienie o zaktualizowanym kernelu dla KDE4.

%prep
%setup -q -n %{appname}

%build
%{__make} \
	INCPATH+="-I/usr/include -I/usr/include/KDE -I/usr/include/qt4/QtCore -I/usr/include/qt4/QtGui -I/usr/include/qt4 -I." \
	LIBS+="-lknotifyconfig -lkworkspace -lkdeui"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/apps/kernelupdatenotifier}
install *.notifyrc $RPM_BUILD_ROOT%{_datadir}/apps/kernelupdatenotifier
install kernelupdatenotifier $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kernelupdatenotifier
%{_datadir}/apps/kernelupdatenotifier
