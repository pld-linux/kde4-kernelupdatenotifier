# TODO
#19:24:47  glen> kernelupdatenotifier.cpp:10:19: error: QObject: No such file or directory
#19:24:47  glen> kernelupdatenotifier.cpp:11:20: error: QProcess: No such file or directory
#19:24:47  glen> kernelupdatenotifier.cpp:12:28: error: QCoreApplication: No such file or directory
# these are missing from kde4-kdelibs-devel?
#19:24:58  glen> /usr/include/kconfigbase.h:29:27: error: QtCore/QtGlobal: No such file or directory
#19:25:05  glen> /usr/include/kconfig.h:31:26: error: QtCore/QString: No such file or directory
#19:25:05  glen> /usr/include/kconfig.h:32:27: error: QtCore/QVariant: No such file or directory
#19:25:05  glen> /usr/include/kconfig.h:33:29: error: QtCore/QByteArray: No such file or directory
#19:25:05  glen> /usr/include/kconfig.h:34:24: error: QtCore/QList: No such file or directory
%define		appname	kernelupdatenotifier
Summary:	Kernel Update Notifier for KDE4
Summary(pl.UTF-8):	Powiadomienie o zaktualizowanym kernelu dla KDE4
Name:		kde4-%{appname}
Version:	1.0
Release:	0.1
License:	LGPL (GPL/GPL v2/GPL v2+... choose one)
Group:		X11/Applications
Source0:	%{appname}-%{version}.tar.gz
# Source0-md5:	dc77fa4e127948a8c305edc5189f9bf0
BuildRequires:	kde4-kdebase-workspace-devel
BuildRequires:	kde4-kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kernel Update Notifier for KDE4

%description -l pl.UTF-8
Powiadomienie o zaktualizowanym kernelu dla KDE4

%prep
%setup -q -n %{appname}

%build
%{__make} \
	INCPATH+="-I/usr/include -I/usr/include/KDE" \
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
