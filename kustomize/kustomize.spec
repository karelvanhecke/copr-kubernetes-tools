%global goipath         sigs.k8s.io/kustomize
%global forgeurl        https://github.com/kubernetes-sigs/kustomize
Version: 5.0.0
%global tag             kustomize/v%{version}

%global gomodulesmode GO111MODULE=on

%gometa

%global commit0 738ca56ccd511a5fcd57b958d6d2019d5b7f2091
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: kustomize
Release: 1%{?dist}
Summary: Customization of kubernetes YAML configurations
License: Apache-2.0
URL: %{gourl}
Source0: %{gosource}

%description
%{summary}

%prep
%goprep -k

%build
export LDFLAGS="-X %{goipath}/api/provenance.version=%{version} \
-X %{goipath}/api/provenance.gitCommit=%{commit0} \
-X %{goipath}/api/provenance.buildDate=$(date -u -d @${SOURCE_DATE_EPOCH} +%FT%TZ) "
%gobuild -o %{gobuilddir}/bin/kustomize %{goipath}/kustomize/v5

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md OWNERS OWNERS_ALIASES code-of-conduct.md CONTRIBUTING.md ARCHITECTURE.md SECURITY_CONTACTS ROADMAP.md
%{_bindir}/*

%changelog
* Fri Feb 10 2023 Karel Van Hecke <copr@karelvanhecke.com> - 5.0.0-1
- Bump to 5.0.0
* Sat Dec 24 2022 Karel Van Hecke <copr@karelvanhecke.com> - 4.5.7-1
- Initial build
