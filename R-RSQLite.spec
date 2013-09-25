%global packname  RSQLite
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.11.4
Release:          1
Summary:          SQLite interface for R
Group:            Sciences/Mathematics
License:          LGPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/RSQLite_0.11.4.tar.gz
Requires:         R-methods R-DBI R-RUnit
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-methods R-DBI R-RUnit
BuildRequires:    sqlite3-devel

%description
Database Interface R driver for SQLite. This package embeds the SQLite
database engine in R and provides an interface compliant with the DBI
package. The source for the SQLite engine (version 3.7.9) is included.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/announce
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/rsqlitePerf.txt
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/HACKING
%doc %{rlibdir}/%{packname}/INSTALL
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/ONEWS
%doc %{rlibdir}/%{packname}/README
%doc %{rlibdir}/%{packname}/THANKS
%doc %{rlibdir}/%{packname}/TODO
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/UnitTests
