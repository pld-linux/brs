Summary:	Bible Retrieval System
Summary(pl.UTF-8):   System Dystrybucji Biblii
Name:		brs
Version:	4.00.l1
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://SunSITE.unc.edu/pub/Linux/apps/religion/%{name}.%{version}.tar.gz
# Source0-md5:	260b789e0ff401293ef05809fc42581b
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Bible Retrieval System consists of a textual database of the
Authorized ("King James") Version of the Old and New Testaments, a set
of libraries for finding and retrieving text, and a program ("bible")
which uses the libraries to retrieve Bible passages given references
on the command line or from standard input. A built-in Concordance
(word search facility) is also supported. A man page is provided.

%description -l pl.UTF-8
The Bible Retrieval System zawiera bazę danych autoryzowanej ("King
James") wersji Starego i Nowego Testamentu. Jest to zestaw bibliotek
do znajdowania i otrzymywania tekstu oraz program ("bible"), który
używa tych bibliotek do otrzymywania wersetów biblii w linii komend lub
ze standardowego wejścia. Wbudowane Concordance (urządzenie do szukania) jest
także wspierane. Dostępna jest strona man.

%prep
%setup -q -n bible

%build
%{__make} \
	CFLAGS="%{rpmcflags} -fwritable-strings -DDESTLIB=\\\"%{_datadir}/%{name}\\\""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_mandir}/man1}

install bible $RPM_BUILD_ROOT%{_bindir}
install bible.data bible.data.conc $RPM_BUILD_ROOT%{_datadir}/%{name}
install bible.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
